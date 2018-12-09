{-# LANGUAGE OverloadedStrings, ScopedTypeVariables #-}

module Main where

import Web.Scotty
import qualified Data.ByteString.Char8 as B
import qualified Data.Text.Lazy as T
import qualified Data.Text as TS
import qualified Data.Text.IO as TIO
import qualified Data.Text.Lazy.Encoding as TE
import Control.Exception (try, SomeException)
import Control.Monad.IO.Class (liftIO)
import Network.HTTP.Types.Status
import System.Environment (getArgs)

-- Reading data
readSource :: FilePath -> IO (Either SomeException T.Text)
readSource p = fmap T.pack <$> try (readFile $ "/home/bikeboi/Wazz/dogdunk/server/data/" ++ p)

-- Transforming data
updateSource :: (FilePath,T.Text) -> IO (Maybe T.Text)
updateSource (fp,t) = do res :: Either SomeException () <- try $ TIO.writeFile ("/home/bikeboi/Wazz/dogdunk/server/data/" ++ fp) $ T.toStrict t
                         return $ case res of
                                    Left se -> Just . T.pack . show $ se
                                    Right _ -> Nothing

-- Error Handling
someErr :: String -> ActionM ()
someErr s = status $ Status 404 (B.pack s)

fileNoExist :: String -> ActionM ()
fileNoExist f = someErr (f ++ " does not exist yet :(")

cantUpdate :: String -> ActionM ()
cantUpdate s = someErr (s ++ " cannot update for some reason :(")

ifExists :: String -> (T.Text -> ActionM ()) -> ActionM ()
ifExists s fma = do fdata <- liftIO $ readSource s
                    case fdata of
                      Left e -> liftIO (putStrLn $ show e) >> fileNoExist s
                      Right x -> fma x

-- Good status
statusOk :: ActionM ()
statusOk = status $ Status 200 "OK"

routes :: ScottyM ()
routes = do get "/:filename" $ do
              filename <- param "filename"
              ifExists filename $ text
            put "/:filename" $ do
              filename <- param "filename"
              content <- body
              val <- liftIO $ updateSource (filename,TE.decodeUtf8 content)
              case val of
                 Nothing -> statusOk
                 Just e -> cantUpdate filename
  where fromEither (Left _) = Nothing
        fromEither (Right x) = Just x

main :: IO ()
main = do
  args <- getArgs
  putStrLn $ "Working in directory: "
  flip ($) routes
    $ case maybeHead args >>= parseInt of -- Quick and dirty cli argument getting
        Just x -> scotty x
        Nothing -> scotty 3000
  where maybeHead [] = Nothing
        maybeHead (x:xs) = Just x
        parseInt x = if all isNum x then Just $ read x
                     else Nothing
        isNum :: Char -> Bool
        isNum c = c `elem` ("1234567890" :: String)
        
